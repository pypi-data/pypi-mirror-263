import mysql.connector

def search_player_info(player_name, year, position):
    try:
        # MySQL 연결 설정
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '12345678',
            'database': 'baseball_stat',
            'auth_plugin': 'mysql_native_password'
        }

        # MySQL 연결
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 테이블 이름 생성
        table_name = f"regular_{year}_{position}"

        # 선수 정보 검색 쿼리 실행
        cursor.execute(f"SELECT * FROM {table_name} WHERE ht_Playername=%s", (player_name,))
        player_info = cursor.fetchone()

        # 연결 및 커서 닫기
        cursor.close()
        conn.close()

        # 결과를 딕셔너리 형태로 반환
        if player_info:
            return {
                '선수 이름': player_info[0],
                '팀': player_info[1],
                '평균 타율': player_info[2],
                '경기': player_info[3],
                '타석': player_info[4],
                '타수': player_info[5],
                '득점': player_info[6],
                '안타': player_info[7],
                '2루타': player_info[8],
                '3루타': player_info[9],
                '홈런': player_info[10],
                '루타': player_info[11],
                '타점': player_info[12],
                '희생번트': player_info[13],
                '희생플라이': player_info[14]
            }

        return None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
