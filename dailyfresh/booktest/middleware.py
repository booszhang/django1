

class UrlMiddleware:

    def process_request(self, request):

        if request.path not in [
            'register',
            'login',
            'login_pwd',
            'login_yz',
            'logout',
            'register_handle',
            'register_hies',

        ]:
            request.session['url_path'] = request.get_full_path()

