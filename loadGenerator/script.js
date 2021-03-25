import http from 'k6/http';
import { sleep } from 'k6';
export default function () {
  http.get('https://vru6pouq2i.execute-api.eu-central-1.amazonaws.com/dev/memmory');
  sleep(1);
}
