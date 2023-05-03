import To_HADOOP
import from_postgre




def main():
    print("Starting stream")
    data = from_postgre.load_from_db()
    To_HADOOP.upload(data)


if __name__ == '__main__':
    main()


