def register_blueprints(app):
    from .main_routes import main_routes
    from .stepper_routes import stepper_routes
    from .servo_routes import servo_routes
    from .scale_routes import scale_routes

    app.register_blueprint(main_routes)
    app.register_blueprint(stepper_routes)
    app.register_blueprint(servo_routes)
    app.register_blueprint(scale_routes)
