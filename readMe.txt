Test task for QApp

К сожалению не удалось нормально реализовать запуск и остановку сервера.
Документация гласит
"Наконец, для запуска локального сервера с нашим приложением, мы используем функцию run(). Благодаря конструкции if __name__ == '__main__' можно быть уверенным, что сервер запустится только при непосредственном вызове скрипта из интерпретатора Python, а не при его импортировании в качестве модуля."
С этим не смог разобраться и в условиях недостатка времени оставил реализацию через test_client
