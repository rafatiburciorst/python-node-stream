import aiofiles
from pathlib import Path
from quart import Quart, request, jsonify, Response, stream_with_context

app = Quart(__name__)

@app.post('/')
async def index():
    try:
        data = await request.get_json()
        dir = Path.cwd()
        file_path = dir / data['filename']

        @stream_with_context
        async def file_generator():
            async with aiofiles.open(file_path, 'rb') as file:  # Open in binary mode for ZIP files
                while True:
                    chunk = await file.read(1024)  # Read in chunks of 64 bytes
                    print(chunk)
                    if not chunk:
                        print('break')
                        break
                    yield chunk

        return Response(file_generator(), content_type='application/zip')
    except Exception as e:
        print('error', e)
        return jsonify({ "message": "hello" }), 500

app.run(host='0.0.0.0', port=5001, debug=True)