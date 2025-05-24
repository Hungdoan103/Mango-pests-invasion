class DatabaseRouter:
    """
    Router điều hướng truy vấn cho các app khác nhau
    """
    surveillance_apps = {'user_auth', 'surveillance', 'surveillance_history'}
    
    def db_for_read(self, model, **hints):
        """Xác định database nào sẽ được dùng để đọc dữ liệu"""
        if model._meta.app_label in self.surveillance_apps:
            return 'surveillance_db'
        return 'default'
    
    def db_for_write(self, model, **hints):
        """Xác định database nào sẽ được dùng để ghi dữ liệu"""
        if model._meta.app_label in self.surveillance_apps:
            return 'surveillance_db'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        """
        Cho phép tạo quan hệ giữa các model nếu chúng thuộc cùng database
        """
        db1 = 'surveillance_db' if obj1._meta.app_label in self.surveillance_apps else 'default'
        db2 = 'surveillance_db' if obj2._meta.app_label in self.surveillance_apps else 'default'
        if db1 == db2:
            return True
        return False
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Xác định model nào được phép migrate trong database nào"""
        if app_label in self.surveillance_apps:
            return db == 'surveillance_db'
        return db == 'default'
