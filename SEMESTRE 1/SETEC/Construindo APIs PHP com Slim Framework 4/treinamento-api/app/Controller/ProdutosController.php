<?php

namespace App\Controller;

use \App\DAO\ConexaoDAO;
use App\DAO\ProdutoDAO;

class ProdutosController{

    public function listar_todos($request, $response, $args){
        $status = '';
        $dados = [];

        try {
            $conexao = new ConexaoDAO();
            $db = $conexao->conectar();
            
            $produtoDAO = new ProdutoDAO($db);
            $dados = $produtoDAO->listar_todos();

            $status = 'sucesso';
            
        } catch (\PDOException $e) {
            $status = 'erro';
        }

        $retorno = ['status' => $status, 'dados' => $dados];

        $response->getBody()->write(json_encode($retorno));
        return $response->withHeader('Content-Type', 'application/json')->withStatus(200);
    }
}