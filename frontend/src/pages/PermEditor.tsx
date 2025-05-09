import {useEffect,useState} from 'react';
import {Table,InputNumber,Button,message} from 'antd';
import {fetchMatrix,saveMatrix} from '../services/permApi';
export default function PermEditor(){
 const [data,set]=useState({});
 useEffect(()=>{fetchMatrix().then(set);},[]);
 const cols=[{title:'Perm',dataIndex:'name'},{title:'Risk',dataIndex:'risk',render:(_,r)=><InputNumber min={1} max={5} value={r.risk} onChange={v=>set(d=>({...d,[r.name]:v}))}/>}]
 const save=async()=>{await saveMatrix(data);message.success('saved')};
 return <div style={{padding:24}}><Table rowKey="name" columns={cols} dataSource={Object.entries(data).map(([name,risk])=>({name,risk}))} pagination={false}/><Button onClick={save}>save</Button></div>;
}
