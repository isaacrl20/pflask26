from dao.db_config import get_connection

class ProfessorDAO:
    sqlSelect = 'SELECT id, nome, disciplinas FROM professor'
    def listar (self):
        conn = get_connection()
        cursor = conn.cursor()
        # Executa consulta SQL
        cursor.execute(self.sqlSelect)
        # Obtém todos os registros
        lista = cursor.fetchall()
        # Fecha conexão
        conn.close()
        return lista