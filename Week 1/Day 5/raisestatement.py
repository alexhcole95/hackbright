import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('raise_statement_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')
