# Python
from typing import Optional

# Langchain Core
from langchain_core.messages import BaseMessage
from langchain_core.language_models import BaseChatModel

# Langchain
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate

# Chatbot Lib
from simple_chatbot_lib.services.models import ContextService
from simple_chatbot_lib.mappers.messages import MessageMapper

class Chatbot:
    """A class to represent a chatbot.

    This class provides methods to initiate a chat with an AI, retrieve the context for a 
    given question, create system and human prompt messages, and retrieve the base messages 
    and tuple messages.

    Attributes:
        llm (BaseChatModel): The language learning model of the chatbot.
        restrictions (list[str]): The restrictions applied to the chatbot.
        personality (str): The personality of the chatbot.
        language (str): The language used by the chatbot.
        message_mapper (MessageMapper): The message mapper used by the chatbot.
        keep_messages (bool): Whether to automatically keep the conversation history or not.
        context_services (Optional[list[ContextService]]): The context services used by the chatbot.
        base_messages (Optional[list[BaseMessage]]): The base messages used by the chatbot.

    Methods:
        chat(question: str) -> str: Initiates a chat with the AI by asking a question and 
        returns the AI's response.
        __create_system_prompt(contexts: list[str]) -> BaseMessage: Creates a system prompt 
        message from a given list of contexts.
        __create_human_prompt(question: str) -> BaseMessage: Creates a human prompt message 
        from a given question.
        __create_introduction() -> BaseMessage: Creates an introduction message based on the 
        chatbot's personality.
        __retrieve_context(question: str) -> list[str]: Retrieves the context for a given 
        question from all context services.
        __call__(question: str) -> str: Calls the chat method with the given question.
    """
    def __init__(self,
                 llm: BaseChatModel,
                 restrictions: list[str],
                 personality: str,
                 language: str,
                 message_mapper: MessageMapper,
                 keep_messages: bool = True,
                 context_services: Optional[list[ContextService]] = None,
                 base_messages: Optional[list[BaseMessage]] = None) -> None:
        """Initializes a new instance of the Chatbot class.

        Args:
            llm (BaseChatModel): The language learning model of the chatbot.
            restrictions (list[str]): The restrictions applied to the chatbot.
            personality (str): The personality of the chatbot.
            language (str): The language used by the chatbot.
            message_mapper (MessageMapper): The message mapper used by the chatbot.
            keep_messages (bool): Whether to automatically keep the conversation history or not.
            context_services (Optional[list[ContextService]]): The context services used by the
            chatbot.
            base_messages (Optional[list[BaseMessage]]): The base messages used by the chatbot.
        """
        self.__llm = llm
        self.__restrictions = restrictions
        self.__personality = personality
        self.__language = language
        self.__message_mapper = message_mapper
        self.__context_services = context_services
        self.__keep_messages = keep_messages

        if base_messages is None or len(base_messages) < 1:
            self.__base_messages = [self.__create_introduction()]
        else:
            self.__base_messages = base_messages

    @property
    def tuple_messages(self) -> list[tuple[str, str]]:
        """Converts the base messages into a list of tuples.

        This property uses the message mapper to convert the list of base messages stored 
        in the __base_messages attribute into a list of tuples. Each tuple contains the 
        type of message and the content.

        Returns:
            list[tuple[str, str]]: A list of tuples where each tuple contains the type 
            of message and the content.
        """
        mapper = self.__message_mapper
        base_messages = self.__base_messages
        return mapper.to_tuple_messages_from(base_messages)

    @property
    def base_messages(self) -> list[BaseMessage]:
        """Gets the base messages.

        This property returns the list of base messages stored in the __base_messages attribute.

        Returns:
            list[BaseMessage]: The list of base messages stored in the __base_messages attribute.
        """
        return self.__base_messages

    def chat(self, question: str) -> str:
        """Initiates a chat with the AI by asking a question and returns the AI's response.

        This method retrieves the context for the given question, creates a system prompt 
        message with the context, creates a human prompt message with the question, and 
        appends these messages to the base messages. It then invokes the AI with the base 
        messages as input and appends the AI's message to the base messages. Finally, 
        it returns the content of the AI's message as a string.

        Args:
            question (str): The question to ask the AI.

        Returns:
            str: The content of the AI's response message.
        """
        has_context = self.__context_services is not None and len(self.__context_services) > 0
        if has_context:
            contexts = self.__retrieve_context(question)
            contexts_system_message = self.__create_contexts_message(contexts)
            self.__base_messages.append(contexts_system_message)
        restrictions_system_message = self.__create_restrictions_message()
        human_message = self.__create_human_prompt(question)
        self.__base_messages.append(restrictions_system_message)
        self.__base_messages.append(human_message)
        ai_message = self.__llm.invoke(input=self.__base_messages)
        if self.__keep_messages:
            self.__base_messages.append(ai_message)
        else:
            self.__base_messages.clear()
        return str(ai_message.content)

    def __create_contexts_message(self, contexts: list[str]) -> BaseMessage:
        template = """Use the information present in the text between
        the <contexts> tags to answer all questions.

        <contexts>
        {contexts}
        <contexts>
        """
        contexts_str = ''
        for index, context in enumerate(contexts):
            contexts_str += f'{index+1} - {context}\n'
        system_prompt_template = SystemMessagePromptTemplate.from_template(template)
        return system_prompt_template.format(contexts=contexts_str)

    def __create_restrictions_message(self) -> BaseMessage:
        template = """Obey the restrictions present in the text
        between the <restrictions> tags.

        <restrictions>
        {restrictions}
        <restrictions>
        """
        restrictions_str = ''
        for index, restriction in enumerate(self.__restrictions):
            restrictions_str += f'{index+1} - {restriction}\n'
        system_prompt_template = SystemMessagePromptTemplate.from_template(template)
        return system_prompt_template.format(restrictions=restrictions_str)

    def __create_human_prompt(self, question: str) -> BaseMessage:
        """Creates a human prompt message from a given question.

        This method uses the given question to create a human message prompt template. 
        It then formats this template to create a human prompt message. The human prompt 
        message is then returned.

        Args:
            question (str): The question to be used to create the human prompt message.

        Returns:
            BaseMessage: A human prompt message created from the given question.
        """
        human_prompt_template = HumanMessagePromptTemplate.from_template(question)
        return human_prompt_template.format()

    def __create_introduction(self) -> BaseMessage:
        """Creates an introduction message based on the chatbot's personality.

        This method uses a template to create a system message prompt. 
        It then formats this template with the chatbot's personality to create a 
        personalized introduction message. The introduction message is then returned.

        Returns:
            BaseMessage: An introduction message personalized with the chatbot's personality.
        """
        template = """You are a chatbot with this personality: {personality}.
        Provide as much detail as possible. Answer in {language}.
        """
        system_prompt_template = SystemMessagePromptTemplate.from_template(template)
        message = system_prompt_template.format(personality=self.__personality,
                                                language=self.__language)
        return message

    def __retrieve_context(self, question: str) -> list[str]:
        """Retrieves the context for a given question from all context services.

        This method iterates over all context services, retrieves the context for 
        the given question from each service, and appends it to a list of contexts. 
        The list of all contexts is then returned.

        Args:
            question (str): The question for which to retrieve the context.

        Returns:
            list[str]: A list of contexts for the given question retrieved from all 
            context services.

        Raises:
            Can raises any Error's from the retrieve_context() method.
        """
        contexts = []
        for context_service in self.__context_services:
            context = context_service.retrieve_context(question)
            contexts.append(context)
        return contexts

    def __call__(self, question: str) -> str:
        return self.chat(question)
