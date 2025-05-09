
import {Layout, Menu} from 'antd';
import {Link} from 'react-router-dom';
export default function SideNav(){
  return (
    <Layout.Sider width={200}>
      <Menu mode="inline" defaultSelectedKeys={['/upload']}>
        <Menu.Item key="/upload"><Link to="/upload">Upload</Link></Menu.Item>
        <Menu.Item key="/tasks"><Link to="/tasks">Tasks</Link></Menu.Item>
        <Menu.Item key="/monitor"><Link to="/monitor">Monitor</Link></Menu.Item>
      </Menu>
    </Layout.Sider>
  );
}
