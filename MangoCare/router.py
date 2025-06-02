class DatabaseRouter:
    """
    Router to direct database queries based on the app.
    - Survey-related apps (user_auth, surveillance, surveillance_history) use surveillance_db
    - All other apps use the default database
    """
    surveillance_apps = {'user_auth', 'surveillance', 'surveillance_history'}
    
    def db_for_read(self, model, **hints):
        """
        Route data reading operations
        """
        if model._meta.app_label in self.surveillance_apps:
            return 'surveillance_db'
        return 'default'
    
    def db_for_write(self, model, **hints):
        """
        Route data writing operations
        """
        if model._meta.app_label in self.surveillance_apps:
            return 'surveillance_db'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models belong to the same database
        """
        app1 = obj1._meta.app_label
        app2 = obj2._meta.app_label
        
        # Allow relations if both belong to the same group
        if app1 in self.surveillance_apps and app2 in self.surveillance_apps:
            return True
        if app1 not in self.surveillance_apps and app2 not in self.surveillance_apps:
            return True
        
        # By default, do not allow relations between models from different databases
        return False
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Only allow migration of surveillance apps to surveillance_db
        and other apps to default database
        """
        if db == 'surveillance_db':
            return app_label in self.surveillance_apps
        elif db == 'default':
            return app_label not in self.surveillance_apps
        return None
