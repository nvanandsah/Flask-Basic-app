from data_server import app


if __name__ == '__main__':
    if app.debug:
        app.run(debug=True, host='0.0.0.0', port=5018)
    else:
        app.run(host='0.0.0.0', port=5018)
