import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/User";
import ToDoList from "./components/Projects";
import axios from 'axios';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'toDoList': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data.results
                console.log(users)
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todos/')
            .then(response => {
                const toDoList = response.data.results
                console.log(toDoList)
                this.setState(
                    {
                        'toDoList': toDoList
                    }
                )
            }).catch(error => console.log(error))
    };


    render() {
        return (
            <div>
                <UserList users={this.state.users}/>
                <ToDoList toDoList={this.state.toDoList}/>
            </div>

        )
    };
}

export default App;
