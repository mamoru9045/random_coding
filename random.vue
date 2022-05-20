<template>
    <div class="main">
        <v-btn @click="do_random()" color="primary">
            <v-icon>mdi-play</v-icon>シャッフル開始
        </v-btn>
    </div>
</template>

<script>
export default {
    name:"main",
    data(){
    },
    methods: {
        do_random(){
            var ans_lists = this.random();

            if(ans_lists[0]){
                console.log(ans_lists[1])
            }else{
                this.do_random()
            }
        },

        random(){
        // グループリストは可変
        var GROUP_LISTS=[
            [1,3],
            [2,4,5,6],
            [7,8,9,10]];
        // 前に選ばれたnumがどこの配列に属していたかを記録する時に必要。
        var random_lst_copy = GROUP_LISTS.slice();
        var ans_list = [];
        ans_list.push(-1)
        var random_list = [];
        var picked_num = 0;
        // 各群をシャッフル
        for(let i=0;i<GROUP_LISTS.length;i++){
            var shuffled = GROUP_LISTS[i].slice();
            random_list.push(this.shuffle(shuffled))
            }
        while(ans_list.length<11){
            // 群を重み付きランダマイズで取得
            var picked_index = this.ProbabilisticChoice(random_list);
            //  前回ans_listに入れた数字の群(リスト)を記録する。(群が連続することは許されない)
            var pre_picked_list = [];
            for (const l of random_lst_copy){
                if(l.includes(ans_list[ans_list.length - 1])){
                    pre_picked_list=l
                }}

            // 強制的に選ぶ必要がある群があるか判定する
            var max_list = []
            var max_list_num = 0;
            var _picked_index = 0;
            for(let i=0;i<random_list.length;i++){
                if(max_list_num < random_list[i].length){
                    max_list_num = random_list[i].length
                    max_list = random_list[i]
                    _picked_index = i
                }
            }

            if((10-ans_list.length)< 2*max_list_num){
                //最も数の多い群から数字を取得
                picked_num = max_list[Math.floor(Math.random() * max_list.length)];
                picked_index = _picked_index
            }else{
                //ランダムな群から数字を取得
                picked_num = random_list[picked_index][Math.floor(Math.random() * random_list[picked_index].length)];   
            }

            if(pre_picked_list.includes(picked_num)){
                if(ans_list.length == 10){
                    // 無限ループに入る
                    console.log('無限ループ')
                    return [false,null]
                }
                continue
            }else{
                // console.log('pre_picked_list',pre_picked_list)
                // console.log('picked_num',picked_num)
                ans_list.push(picked_num)

                var index = random_list[picked_index].findIndex(n => n === picked_num);
                random_list[picked_index].splice(index, 1)
            }
        }
        return [true,ans_list.slice(1)]
        },
        // 単純なシャッフル
        shuffle(array){
            var list = array;
            for (let i=list.length - 1 ;i>=0 ;i--){
                const j = Math.floor(Math.random()*(i+1));
                [list[i],list[j]] = [list[j],list[i]];
            }
            return list
            },
        // リストの長いものから取得する関数（重みつけ）
        ProbabilisticChoice(array){
            var lists = array;
            var totalWeight = this.total(array);
            var r = Math.random()*totalWeight;
            var s=0.0;
            for(let j=0;j<lists.length;j++){
                s+=lists[j].length;
                if(r<s){
                    return j
                }
            }
        },
        // 2次配列の要素数
        total(array){
            var sum = 0;
            for(const a of array){
                sum+=a.length
            }
        return sum
        }
    },
    
}
</script>
