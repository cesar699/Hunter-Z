import { Switch, Tooltip, message } from 'antd';
import { EyeInvisibleOutlined, EyeOutlined } from '@ant-design/icons';
import { useState } from 'react';
import { useTranslation } from 'react-i18next';

export default function TorSwitch() {
  const { t } = useTranslation();
  const [on,setOn] = useState(false);
  const [loading,setLoading]=useState(false);
  const toggle = async(checked:boolean)=>{
    setLoading(true);
    await fetch(`/proxy/tor/${checked?'on':'off'}`,{method:'POST'});
    message.success(checked?t('tor_on'):t('tor_off'));
    setOn(checked);setLoading(false);
  };
  return (
    <Tooltip title={on?t('anonymous_on'):t('anonymous_off')}>
      <Switch checked={on} onChange={toggle} loading={loading}
        checkedChildren={<EyeInvisibleOutlined/>}
        unCheckedChildren={<EyeOutlined/>}/>
    </Tooltip>
  );
}
