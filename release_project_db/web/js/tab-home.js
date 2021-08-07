let VISIBLE_DB_HOME = false;
// Функція показу бази данних на головній сторінці
eel.expose(get_dbs);
 function get_dbs(data_tables, name_columns){
   mydata = data_tables;
   title_name = name_columns;
   if (VISIBLE_DB_HOME == false){
     VISIBLE_DB_HOME = true;
     let parent = document.getElementById('contents');
     let povt = document.getElementById('povtor');
     
     if(!povt){
       let table_tr = document.createElement('tr');
       
       // Цикл показу заголовків бази данних
       for(let iter_name = 0; iter_name < title_name.length; iter_name++){
         let table_th = document.createElement('th');
         let name_col = title_name[iter_name][0];
         table_th.innerHTML = name_col;
         table_th.setAttribute("scope", "col");
         table_th.setAttribute("class", "title-js");
         parent.appendChild(table_tr);
         table_tr.appendChild(table_th);
        }
        //Цикл показу контенту з БД
        for(let i = 0; i < mydata.length; i++){
          let parent = document.getElementById('contents');
          let table_tr = document.createElement('tr');
          table_tr.setAttribute("id", "povtor");
          table_tr.setAttribute("class", "uio");
          
          for(let j = 0; j < mydata[0].length; j++){
            let table_td = document.createElement('td');
            let name = mydata[i][j];
            table_td.innerHTML = name;
            table_td.setAttribute("scope", "row"); 
            table_td.setAttribute("class", "uio2");
            parent.appendChild(table_tr);
            table_tr.appendChild(table_td);
          }
        }
      }

   }
    
    }
    // Обробляє кнопку "Показати базу данних"
    function clc(){
      eel.click_db();
    }
    // Видаляє базу з головної сторінки
    function del_clc(){
      VISIBLE_DB_HOME = false;
      let title_db = document.getElementsByClassName('title-js');
      let row_db = document.getElementsByClassName('uio');
      
      for(let t = 0; t < title_db.length; t++){
        title_db[t].remove();
        t--;
      }

      let l = row_db.length
      for(let del_row = 0; del_row < l; del_row++){
        row_db[del_row].remove();
        del_row--;
      }
    }