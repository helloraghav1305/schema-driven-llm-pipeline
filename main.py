from retry_handler import output_with_retry

if __name__ == '__main__':
    email = 'Hi, I was charged twice for my last invoice. Please help to fix this.'

    result = output_with_retry(email)

    print('\n Final Output:')
    print(result)