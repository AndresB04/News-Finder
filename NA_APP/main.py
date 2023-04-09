from website import News_Finder

app = News_Finder()

if __name__ == '__main__':
    app.run(debug=True, port=8000)