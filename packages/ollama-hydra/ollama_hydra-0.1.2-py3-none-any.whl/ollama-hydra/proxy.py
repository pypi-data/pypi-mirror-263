import asyncio
import requests
import ollama
from time import sleep

model_port_mappings = {}  
litellm_base_url = "http://localhost:"
next_available_port = 8001  # Starting port for dynamic assignment

async def handle_request(reader, writer):
    try:
        request_line = await reader.readline()
        method, path, _ = request_line.decode().strip().split()

        headers = {}
        while True:
            header_line = await reader.readline()
            if header_line == b'\r\n':
                break
            header_key, header_value = header_line.decode().strip().split(':', 1)
            headers[header_key] = header_value.strip()

        target_host, target_port = model_port_mappings[writer.get_extra_info('peername')[1]]
        forward_url = litellm_base_url + str(target_port) + path

        response = requests.request(method, forward_url, headers=headers, stream=True)

        writer.write(f"HTTP/1.1 {response.status_code} {response.reason}\r\n".encode())
        for header in response.headers.items():
            writer.write(f"{header[0]}: {header[1]}\r\n".encode())
        writer.write(b'\r\n')

        for chunk in response.iter_content(1024):
            if not chunk:
                break
            writer.write(chunk)

        await writer.drain()
        writer.close()

    except Exception as e:
        print(f"Error handling request: {e}")

async def update_model_mappings():
    """Updates the model_port_mappings dictionary using ollama.list()."""
    global model_port_mappings, next_available_port

    while True:
        try:
            models = ollama.list()
            new_mappings = {}
            for model in models:
                port = next_available_port
                next_available_port += 1
                new_mappings[port] = (model['name'], port)   

            model_port_mappings = new_mappings

        except Exception as e:
            print(f"Error updating model mappings: {e}")

        sleep(30)  # Adjust update interval as needed

async def main():
    asyncio.create_task(update_model_mappings())

    tasks = [asyncio.start_server(handle_request, host='0.0.0.0', port=port) 
             for port in model_port_mappings.keys()]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
