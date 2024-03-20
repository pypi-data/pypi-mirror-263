import openai
import instructor
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
from datasets import Dataset
from random import sample

load_dotenv()


class ExtractQA(BaseModel):
    """Class for question and answer schema"""

    question: str = Field(
        description="Specific and relevant question from the text."
    )
    answer: str = Field(
        description="Specific and accurate answer to the question generated from text."
    )


MultiQA = instructor.IterableModel(ExtractQA)


def get_qa(dataset, num_questions: int) -> Dataset:
    client = instructor.patch(
        openai.OpenAI(
            base_url="https://api.endpoints.anyscale.com/v1",
            api_key=os.getenv("ANYSCALE_PER"),
        )
    )
    proc_dataset = dataset.shuffle().select(range(num_questions))
    output_list = []
    for i in range(len(proc_dataset)):
        text = proc_dataset["text"][i]
        chat_completions = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            response_model=MultiQA,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Generate specific questions from the following text:\n\n# Text:\n{text}",
                },
            ],
            max_retries=4,
        )
        questions = [x.question for x in chat_completions]
        answers = [x.answer for x in chat_completions]
        if len(questions) == len(answers):
            zip_qa = [(x, y) for x, y in zip(questions, answers)]
        for tup in zip_qa:
            new_dict = {
                "chunk_id": proc_dataset["chunk_id"][i],
                "text": proc_dataset["text"][i],
                "question": tup[0],
                "answer": tup[1],
            }
            output_list.append(new_dict)

    return Dataset.from_list(output_list)
