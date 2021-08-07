let VISIBLE_DB_EDIT = false;
// Блок коду відповідальний за редагування бази данних
eel.expose(edit_db_in)
function edit_db_in(cont, col_name){
  data = cont;
  title = col_name;
  if (VISIBLE_DB_EDIT == false){
    VISIBLE_DB_EDIT = true
    // @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    let container_from_table = document.getElementById('insert-table');

    let id_table = document.createElement('table');
    id_table.setAttribute("class", "table")
    id_table.setAttribute("id", "tableeditdb")
    container_from_table.appendChild(id_table)

    // Цикл показу заголовків бази данних
    let table_tr = document.createElement('tr');
    let empty_cell = document.createElement('th');
    table_tr.appendChild(empty_cell);
    for(let iter_name = 0; iter_name < title.length; iter_name++){
      let table_th = document.createElement('th');
      let name_col = title[iter_name][0];
      table_th.innerHTML = name_col;
      table_th.setAttribute("scope", "col");
      table_th.setAttribute("class", "title-js-edit");
      id_table.appendChild(table_tr);
      table_tr.appendChild(table_th);
      }
      
      // Цикл показу інформації з бази данних
      for (i = 0; i < data.length; i++){
        let create_row = document.createElement("tr");
        create_row.setAttribute("class", "del-rows");
        let del_button = document.createElement("button");
        del_button.innerHTML = 'X';
        del_button.setAttribute("class", "btn btn-danger")
        create_row.appendChild(del_button);
        for(j = 0; j < data[0].length; j++){
          
          del_button.setAttribute("id", data[i][0]);
          del_button.setAttribute("onClick", "row_delete(this)")
          let create_col = document.createElement('td');
          id_table.appendChild(create_row);
          create_row.appendChild(create_col);
                
          let create_text = document.createElement("INPUT");
          create_text.setAttribute("type", "text");
          create_text.setAttribute("value", data[i][j]);
          create_text.setAttribute("class", "form-control");
          create_text.setAttribute("id", "gg");
          create_col.appendChild(create_text);
        }
      }
    // @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  }
  }
        // Обробляє кнопку "Редагувати базу данних"
        function edit_db(){
          eel.edit_db_python();
        }

// Видаляє базу з головної сторінки
function del_edit_db(){
  VISIBLE_DB_EDIT = false;
  let title_db = document.getElementById('tableeditdb');
  title_db.remove();
  }        

  // Викликає функцію send_value_db з пайтона
  function button_add_row(){
    eel.send_value_db()
  }
  
  // Додає рядок
  eel.expose(add_row)
  function add_row(values_db){
    row_len = values_db[0].length;
    
    value_len = values_db.length;
    old_id = values_db[value_len - 1][0];
    let new_id = old_id + 1;
    let create_v_id = document.createElement('INPUT');
    create_v_id.setAttribute("value", new_id);
    
    let id_table = document.getElementById('tableeditdb');
    let create_row = document.createElement("tr");
    let ttt = document.createElement('td');
    create_v_id.setAttribute("class", "form-control")
    create_row.appendChild(ttt);
    create_row.appendChild(create_v_id);
    for(i = 1; i < row_len; i++){
      let create_col2 = document.createElement('td');
      create_col2.setAttribute("class", "title-js-edit");
      id_table.appendChild(create_row);
      create_row.appendChild(create_col2);
      let create_text = document.createElement("INPUT");
      create_text.setAttribute("type", "text");
      create_text.setAttribute("value", 'null');
      create_text.setAttribute("class", "form-control");
      create_text.setAttribute("id", "gg");
      create_col2.appendChild(create_text);
    }
    let set_value = [];
    for(j = 0; j < row_len; j++){
      set_value.push(j)
    }
    eel.add_rows(set_value);
    del_edit_db();
    edit_db();
  }

  function row_delete(obj){
    eel.delete_row(obj.id);
    del_edit_db();
    edit_db();
  }