class StringFormatter(object):

    @staticmethod
    def del_word(text, n):
        return ' '.join([word for word in text.split(' ') if len(word) > n])

    @staticmethod
    def replace_digit(text):
        return text.translate(text.maketrans("123456789","*********"))

    @staticmethod
    def insert_space(text):
        return ' '.join([i for i in ' '.join(text)])

    @staticmethod
    def sort_size(text):
        return ' '.join(sorted(text.split(), key = len))

    @staticmethod
    def sort_alphabet(text):
        return ' '.join(sorted(text.split()))