    if (check_randmize(GROUP_LISTS,random_lists)){
        console.log('')
    }else{console.log('ランダマイズ失敗')}
    
    
//  ランダマイズチェッカー
function check_randmize(GROUP_LISTS,random_list){
    for(let i=0;i<random_list.length-1;i++){
        var n = random_list[i];
        var pre_picked_list = [] ;
        for(const l of GROUP_LISTS){
            if(l.includes(n)){
                pre_picked_list = l
            }
        }
        if (pre_picked_list.includes(random_list[i+1])){
            return false
        }
    }
    return true
}
