from openai import OpenAI


class Assistant:
    def __init__(self):
        self.client = OpenAI(api_key='<TWÓJ KOD API>')

        self.assistant = self.client.beta.assistants.create(
            name='Python Mentor',
            instructions='Jesteś mentorem, który pomaga mi w nauce Pythona. Tłumacz w prosty, zrozumiały sposób.',
            tools=[{"type": "code_interpreter"}],
            model='gpt-4o'
        )

        self.thread = self.client.beta.threads.create()

    def send_message(self, message):
        self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=message
        )

        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
            instructions="Zwracaj się do użytkownika jako Kamil"
        )

        if run.status == 'completed':
            messages = self.client.beta.threads.messages.list(
                thread_id=self.thread.id
            )
            return messages.data[0].content[0].text.value
        else:
            return run.status
