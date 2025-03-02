from tokeo.ext.appshare import app


@app.nicegui.fastapi_app.get('/api')
async def get_api():
    return {'msg': 'spiral json api result'}
