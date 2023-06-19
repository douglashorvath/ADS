<?php
namespace App\DAO;

final class ConexaoDAO{

    public static function conectar(){
        $host = getenv('DB_HOST');
        $user = getenv('DB_USER');
        $pass = getenv('DB_PASS');
        $dbname = getenv('DB_NAME');

        $pdo = new \PDO("mysql:host={$host};dbname={$dbname}", $user, $pass);
        $pdo->exec("SET CHARACTER SET utf8");
        $pdo->setAttribute(\PDO::ATTR_ERRMODE, \PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(\PDO::ATTR_DEFAULT_FETCH_MODE, \PDO::FETCH_ASSOC);

        return $pdo;
    }
}