from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve, reverse, Resolver404
from django.contrib import messages
import re

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # URLs that don't require login
        self.exempt_urls = [
            # Home page
            re.compile(r'^/$'),
            re.compile(r'^$'),
            # Login and registration pages
            re.compile(r'^/auth/login/?$'),
            re.compile(r'^/auth/register/?$'),
            # Static resources and media
            re.compile(r'^/static/.*$'),  # All static files
            re.compile(r'^/media/.*$'),   # All media files
            re.compile(r'.*\.css$'),       # CSS files
            re.compile(r'.*\.js$'),        # JavaScript files
            re.compile(r'.*\.png$'),       # PNG images
            re.compile(r'.*\.jpg$'),       # JPG images
            re.compile(r'.*\.jpeg$'),      # JPEG images
            re.compile(r'.*\.gif$'),       # GIF images
            re.compile(r'.*\.svg$'),       # SVG images
            re.compile(r'.*\.ico$'),       # Icon files
            re.compile(r'.*\.woff$'),      # Font files
            re.compile(r'.*\.woff2$'),     # Font files
            re.compile(r'.*\.ttf$'),       # Font files
            re.compile(r'.*\.eot$'),       # Font files
            # Misc
            re.compile(r'^/favicon\.ico$'),
        ]
        
        # Names of URLs that are exempt from login requirement
        self.exempt_url_names = [
            'home',  # Home page
            'login',  # Login page
            'register',  # Registration page
        ]

    def __call__(self, request):
        # If the user is already logged in, allow access to all pages
        if request.user.is_authenticated:
            return self.get_response(request)

        # Check the current path
        current_path = request.path_info
        
        # Check if it's a static resource
        if '/static/' in current_path or '/media/' in current_path or current_path.split('.')[-1] in ['css', 'js', 'png', 'jpg', 'jpeg', 'gif', 'svg', 'ico', 'woff', 'woff2', 'ttf', 'eot']:
            return self.get_response(request)
        
        # Direct check if it's the home page (most common case)
        if current_path == '/' or current_path == '':
            return self.get_response(request)
        
        # Check URL name
        try:
            url_name = resolve(current_path).url_name
            if url_name in self.exempt_url_names:
                return self.get_response(request)
        except Resolver404:
            pass
        
        # Check URLs that are exempt from login
        for pattern in self.exempt_urls:
            if pattern.match(current_path.lstrip('/')) or pattern.match(current_path):
                return self.get_response(request)
        
        # For other URLs, require login
        return redirect(settings.LOGIN_URL)


class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process access control logic before the request is processed
        # Check if user is authenticated and tries to access surveillance module (not surveillance_history)
        if request.user.is_authenticated and request.path.startswith('/surveillance/') and not request.path.startswith('/surveillance_history/'):
            # If the user has a viewer role, do not allow access to surveillance module
            if request.user.is_viewer_user:
                # Redirect to home page and display a message
                messages.error(request, 'You do not have permission to access the Surveillance feature.')
                return redirect(reverse('home'))
        
        # Pass the request to the next view or middleware
        response = self.get_response(request)
        return response
