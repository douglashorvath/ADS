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
            $dados = $result->fetchAll(\PDO::FETCH_OBJ);
        }

        return $dados;
    }

    public function buscar_por_id($prod_id){
    }

    public function cadastrar($dados){
    }

    public function atualizar($dados){
    }

    public function remover($prod_id){
    }
}
