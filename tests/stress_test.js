import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
    insecureSkipTLSVerify: true,
    noConnectionReuse:false,
    stages: [
        {duration: '2m', target: 100}, //below normal load
        {duration: '5m', target: 100},
        {duration: '2m', target: 200}, // normal load
        {duration: '5m', target: 200},
        {duration: '2m', target: 300}, // around expected breaking point
        {duration: '5m', target: 300},
        {duration: '2m', target: 400}, // beyond expected breaking point
        {duration: '5m', target: 400},
        {duration: '10m', target: 0}, // scale down. Attempt Recovery
    ]

};

export default () => {
    http.get('http://localhost:8051');
    sleep(2);
  }