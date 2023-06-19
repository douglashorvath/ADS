<?php
use Slim\Factory\AppFactory;

require __DIR__ . '/vendor/autoload.php';

$app = AppFactory::create();
$app->addBodyParsingMiddleware();
$app->addRoutingMiddleware();
$errorMiddleware = $app->addErrorMiddleware(true, true, true);

require __DIR__ . '/app/config.php';
require __DIR__ . '/app/routes.php';

$app->setBasePath("/treinamento-api");
$app->run();
