<?php

namespace App\Controller;

use \App\DAO\ConexaoDAO;
use App\DAO\ProdutoDAO;
use Exception;

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

    //Variáveis $request, $response e $args são padrão do framework
    public function cadastrar($request, $response, $args){
        $status = null;
        $mensagem = null;
        
        $data = (object)$request->getParsedBody();
        try{
            $conexao = new ConexaoDAO();
            $db = $conexao->conectar();

            /*
            Caso use uma classe para produtos chamada ProdutosModel
            $produtos = new ProdutosModel();
            $produtos->setNome($data->prod_nome);
            Depois manda a variável $produtos ao invés de $data
            */

            $produtoDAO = new ProdutoDAO($db);
            $produtoDAO->cadastrar($data);

            $status = "sucesso";
            $mensagem = "Produto cadastrado com sucesso";
        }
        catch(Exception $e){
            $status = "erro";
            $mensagem = $e->getMessage();
        }

        //variável de retorno
        $retorno = ["status" => $status, "mensagem"=>$mensagem];
        //retorna para o solicitante usando JSON
        $response->getBody()->write(json_encode($retorno));
        return $response->withHeader('Content-Type', 'application/json')->withStatus(201);

    }
}