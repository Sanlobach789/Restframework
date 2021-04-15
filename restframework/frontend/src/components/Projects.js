import React from "react";

const ToDoItem = ({toDoItem}) => {
    return (

        <tr>
            <td>
                {toDoItem.project.name}
            </td>
            <td>
                {toDoItem.title}
            </td>
            <td>
                {toDoItem.content}
            </td>
            <td>
                {toDoItem.author.username}
            </td>
            <td>
                {toDoItem.created}
            </td>
        </tr>

    )
}

const ToDoList = ({toDoList}) => {
    return (
        <table>
            <thead>
            <tr>
                <th>
                    Проект
                </th>
                <th>
                    Наименование
                </th>
                <th>
                    Содерждание
                </th>
                <th>
                    Автор
                </th>
                <th>
                    Дата создания
                </th>
            </tr>
            </thead>
            <tbody>
            {toDoList.map((toDoItem)=><ToDoItem toDoItem={toDoItem} key={toDoItem.id}/>)}
            </tbody>
        </table>
    )
}

export default ToDoList