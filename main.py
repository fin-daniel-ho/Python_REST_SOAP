# Module main.
# Description: Create and run the application.
# Author : Dung Ho
# Email: dung.ho@edu.turkuamk.fi


import logging
from app import create_app


# Create an application
app = create_app()


# Run the app with Debug mode and print out useful information
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info('listening to http://127.0.0.1:5000')
    logging.info('Homepage is at: http://127.0.0.1:5000/index')
    logging.info('wsdl is at: http://127.0.0.1:5000/soap?wsdl')

    app.run(debug=True)
