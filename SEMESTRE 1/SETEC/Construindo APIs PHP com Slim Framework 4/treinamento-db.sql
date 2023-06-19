-- -----------------------------------------------------
-- Schema treinamento-api
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `treinamento-api` DEFAULT CHARACTER SET utf8 ;
USE `treinamento-api` ;

-- -----------------------------------------------------
-- Table `treinamento-api`.`produtos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `treinamento-api`.`produtos` (
  `prod_id` INT NOT NULL AUTO_INCREMENT,
  `prod_nome` VARCHAR(100) NOT NULL,
  `prod_marca` VARCHAR(100) NOT NULL,
  `prod_fornecedor` VARCHAR(100) NOT NULL,
  `prod_estoque` INT NOT NULL,
  `prod_data_cadastro` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `prod_data_atualizacao` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`prod_id`))
ENGINE = InnoDB;