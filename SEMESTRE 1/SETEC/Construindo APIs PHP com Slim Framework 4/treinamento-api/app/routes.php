<?php
use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;


$app->get('/api/ola_mundo', function (Request $request, Response $response, $args){
    $response->getBody()->write(json_encode('Olá mundo.'));
    return $response->withHeader('Content-Type', 'application/json');
});