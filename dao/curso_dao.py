from dao.db_config import get_connection 



class CursoDAO:
    sqlSelect = 'SELECT id, nome_curso , duracao FROM curso'
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
    def salvar(self, id, nome_curso, duracao):
            conn = get_connection()
            cursor = conn.cursor()
            try:
                cursor.execute(
                    'INSERT INTO curso (nome_curso, duracao) VALUES (%s, %s)',
                    (nome_curso, duracao)
                )
                conn.commit()
                return {"status": "ok"}
            except Exception as e:
                return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
            finally:
                conn.close()
