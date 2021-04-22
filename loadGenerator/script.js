import http from 'k6/http';
import { sleep } from 'k6';
export default function () {
  http.get('https://0yfgitcbj8.execute-api.eu-central-1.amazonaws.com/dev/cpu_intensive');
  sleep(1);
}
