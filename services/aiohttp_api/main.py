from aiohttp import web


if __name__ == '__main__':
    async def hello(request):
        a = request.query.get("a")
        if str(a).isdigit():
            return web.Response(text=f"a in square is {int(a)**2}")
        return web.Response(text=f"a is not a digit, or not presented")

    app = web.Application()
    app.add_routes([web.get('/', hello)])
    web.run_app(app)
