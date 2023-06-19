<?php
namespace App\DAO;

class ProdutoDAO{
    /** @var string */
    protected $table;

    /** @var \PDO */
    protected $db;

    public function __construct($db){
        $this->table = "produtos";
        $this->db = $db;
    }

    public function listar_todos(){
        $dados = null;
        $sql  = "SELECT * FROM {$this->table}";

        $result = $this->db->prepare($sql);
        $result->execute();

        if ($result->rowCount() > 0) {
            //formato de objeto
            $dados = $result->fetchAll(\PDO::FETCH_OBJ);
        }

        return $dados;
    }

    public function buscar_por_id($prod_id){
    }

    public function cadastrar($dados){
        
        /*
        $sql = "INSERT INTO {this->table} (prod_nome,prod_marca,prod_fornecedor,prod_estoque) VALUES (?,?,?,?)";
        $result = $this->db->prepare($sql);
        $result->bindValue(1,$dados->prod_nome);
        $result->bindValue(2,$dados->prod_marca);
        $result->bindValue(3,$dados->prod_fornecedor);
        $result->bindValue(4,$dados->prod_estoque);*/

        //pode ser usado com identificadores
        $sql = "INSERT INTO {$this->table} (prod_nome,prod_marca,prod_fornecedor,prod_estoque) VALUES (:prod_nome,:prod_marca,:prod_fornecedor,:prod_estoque)";
        $result = $this->db->prepare($sql);
        $result->bindValue(":prod_nome",$dados->prod_nome);
        $result->bindValue(":prod_marca",$dados->prod_marca);
        $result->bindValue(":prod_fornecedor",$dados->prod_fornecedor);
        $result->bindValue(":prod_estoque",$dados->prod_estoque);
        
        

        $result->execute();
    }

    public function atualizar($dados){
    }

    public function remover($prod_id){
    }
}
