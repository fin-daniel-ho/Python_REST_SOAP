# Module soap.
# Description: Create a SOAP server and create_message service.
# Author : Dung Ho
# Email: dung.ho@edu.turkuamk.fi


from spyne.application import Application
from spyne.decorator import srpc
from spyne.model.complex import ComplexModel, Array
from spyne.model.primitive import Mandatory
from spyne.server.wsgi import WsgiApplication
from spyne.service import ServiceBase
from spyne.protocol.soap import Soap11
from instances.config import messages


class Message(ComplexModel):
    """
    Create a Message model with its attributes.

    :return: a Complex object.
    """
    __namespace__ = 'message_board.soap'
    _type_info = {
        "title": Mandatory.Unicode(encoding='utf-8', max_len=20),
        'content': Mandatory.Unicode(encoding='utf-8', max_len=200),
        "sender": Mandatory.Unicode(encoding='utf-8', max_len=30),
        "url": Mandatory.AnyUri(encoding='utf-8', max_len=100),
    }


class AddMessageService(ServiceBase):
    """
    This service is used for creating a message.
    """

    @srpc(Message, _returns=Array(Message))
    def create_message(message):
        """
        Create a message from the query parameters.

        :param message: set as namespace in Soap11 request body.

        :return: an array of Message object.
        """

        msg = {
            'title': message.title,
            'content': message.content,
            'sender': message.sender,
            'url': message.url
        }

        messages.append(msg)

        return messages


# Create wsgi application
application = Application(
    [AddMessageService],
    tns='message_board.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

wsgi_application = WsgiApplication(application)
