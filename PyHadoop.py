from hdfs import InsecureClient  # hdfs 모듈에서 webhdfs로 모듈 임포트

#접속테스트

client = InsecureClient('http://192.168.56.3:50070', user='hadoop')
print(client.status)

def list_files(path):  # path 경로 내의 파일을 출력
    files = client.list(path)

    if len(files) == 0:
        print('File not found')
    else:
        for file in files:
            print('File:', file)

def makedir_test(path):
    '''path 경로를 hdfs에 생성'''
    client.makedirs(path)

def delete_test(path, r=True):
    #recursive=True : 디렉토리의 경우 하위 티렉토리도 함께 삭제
    client.delete(path, recursive=r)

def write_test(path, text, encoding='utf=8'):
    # 리스트 파일즈 이그잼플 / 아래파일 목록을 출력
    with client.write(path, encoding=encoding) as writer:
        writer.write(text)
        
def read_test(path, encoding='utf=8'):
    '''path 경로 파일을 읽어서 출력'''
    with client.read(path, encoding=encoding) as reader:
        data = reader.read()
    print('hadoop read:', data)


if __name__ == '__main__':
    # list_files('/example') /이하의 파일 목록을 출력
    makedir_test('/example/PyHadoop')
    # write_test('example/myhadoop/test.txt', 'hello hadoop')
    # read_test('example/myhadoop/test.txt')
    # delete_test('example/myhadoop/')