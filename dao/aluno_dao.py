from dao.db_config import get_connection

class AlunoDAO:
    sqlSelect = 'SELECT id, nome, idade, cidade FROM aluno'

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        # Executa consulta SQL
        cursor.execute(self.sqlSelect)
        # Obtém todos os registros
        lista = cursor.fetchall()
        # Fecha conexão
        conn.close()
        return lista

    def salvar(self, id, nome, idade, cidade):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO aluno (nome, idade, cidade) VALUES (%s, %s, %s)',
                (nome, idade, cidade)
            )
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
