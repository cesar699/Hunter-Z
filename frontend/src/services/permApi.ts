export const fetchMatrix = async()=> (await (await fetch('/perm/')).json());
export const saveMatrix = async(data)=> fetch('/perm/',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
