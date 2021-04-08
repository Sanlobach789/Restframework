import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from "./components/User";
import ToDoList from "./components/Projects";
import axios from 'axios';
import Projects from "./components/Projects";
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'
import LoginForm from "./components/Auth";
import Cookies from "universal-cookie/lib";

const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу {location.pathname} не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'toDoList': [],
            'token': '',
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token})
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token})
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password}.then(
            response => {this.set_token(response.data['token'])
            }).catch(error => alert('Wrong username or password'))
        )
    }

    load_data() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todos/')
            .then(response => {
                const toDoList = response.data.results
                this.setState(
                    {
                        'toDoList': toDoList
                    }
                )
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
        this.load_data()
    };


    render() {
        return (
            <div className="App">
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/users'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> :
                                    <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/users' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' component={() => <ToDoList toDoList={this.state.toDoList}/>}/>
                        <Route exact path='/login' component={() => <LoginForm get_token={
                                (username, password) => this.get_token(username, password)}
                            />}
                        />
                        <Redirect from='/todos' to='projects/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
            </div>

        )
    };
}

export default App;
