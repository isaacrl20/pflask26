from dao.db_config import get_connection


class AlunoDAO:
    sqlSelect='SELECT id, nome, idade, cidade FROM aluno'
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