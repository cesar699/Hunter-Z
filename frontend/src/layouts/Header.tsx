import { Layout } from 'antd';
import TorSwitch from '../components/TorSwitch';
export default function HeaderBar(){
  return <Layout.Header style={{background:'#fff',padding:'0 16px',textAlign:'right'}}>
    <TorSwitch/>
  </Layout.Header>;
}
