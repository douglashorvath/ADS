<?php

namespace App\Controller;

use Firebase\JWT\JWT;

class TokenController{


    public function gerar_token($request, $response, $args){
        
        //expiração do token, somando x minutos ao horário atual
        $date = (new \DateTime())->modify('+30 minute');

        //criando payload
        $tokenPayload = [
            'sub' => mt_rand(100,999),
            'exp' => $date->getTimestamp()
        ];

        //sempre passar payload e segredo. Segredo está no arquivo config.php usando variáveis de ambiente
        $token = JWT::encode($tokenPayload,getenv('JWT_SECRET'));

        $retorno = ['token' => $token];
        $response->getBody()->write(json_encode($retorno));
        return $response->withHeader('Content-Type', "application/json");


    }
}