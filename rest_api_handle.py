class rest_api_handler():
    def __init__(self):
            m1.value(0)
            m2.value(0)

    def on(self):
        print("ALEXA ABRE LA CORTINA ")
        m1.value(1)
        m2.value(0)           
        return True

    def off(self):
        print("ALEXA CIERRA LA CORTINA ")
        m1.value(0)
        m2.value(1)
        return True            
