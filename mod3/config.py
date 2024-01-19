import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    server_name = os.environ.get('SERVER_NAME')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET-KEY'
    AWS_ACCESS_KEY_ID = "ASIARO43Q7UGBFYCRZ7L"
    AWS_SECRET_ACCESS_KEY = "CGhPZaZTiXCEqMfOY+yQmCQeR3W6KRktSoZ8CDD6"
    AWS_SESSION_TOKEN = "FwoGZXIvYXdzEFMaDB/tRZnFvV3baNwy8iLLAYqEX8xqnL24hltxbD65rV/doOHW8eEmrnvImpsy+nRaJnrxmhO9OE/OcIswa7CXgpf+vnNwR8NjQsnOgOz06gztkspA1EmpPo0jsVMvZ1VBJiWSGAi73VnbjdhOMZn2ZICfoxBzu3pFVHDqgP/+pCpE11He5qB8LYbDygefCPQEXX7KtdY5pRhA918zZH52dVTRcKOZ7E+rFQsOTiywzqTaChIHN1KSq7JURnkcoN4WeSV74yBKMCUwfTKYtIfMCUP7DkuBlnvHigh7KNaLqa0GMi3NAmZnwueXjR3F5z2J8EVK8OEL1gTDxWRS+VMaY2qw+09TxorXVQfYeRVM0h8="
