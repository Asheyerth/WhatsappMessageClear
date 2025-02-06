import axios from 'axios';

export default axios.create({
    baseURL: 'http://localhost:5000'//,
    //baseURL: 'http://127.0.0.1:5000'//,
    //headers: {
    //    'Content-Type': 'application/json',
    //    'Access-Control-Allow-Origin': '*'
    //    'Authorization': "JWT " + localStorage.getItem('token')
    //}//,
    //xsrfCookieName: 'csrftoken',
    //xsrfHeaderName: 'X-CSRFToken',
    //withCredentials: true
});