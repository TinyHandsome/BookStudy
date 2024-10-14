package com.sxt.Server_study03;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author: Li Tian
 * @contact: litian_cup@163.com
 * @software: IntelliJ IDEA
 * @file: WebContext.java
 * @time: 2019/12/3 10:51
 * @desc:
 */

public class WebContext {
    private List<Entity> entitys = null;
    private List<Mapping> mappings = null;

    // key-->servlet-name  value-->servlet-class
    private Map<String, String> mappingMap = new HashMap<>();
    // key-->url-pattern  value-->servlet-name
    private Map<String, String> entityMap = new HashMap<>();

    public WebContext(List<Entity> entitys, List<Mapping> mappings) {
        this.entitys = entitys;
        this.mappings = mappings;

        // 将entity的List转成了对应的map
        for(Entity entity: entitys){
            entityMap.put(entity.getName(), entity.getClz());
        }
        // 将map的List转成了对应的map
        for(Mapping mapping: mappings){
            for(String pattern: mapping.getPatterns()){
                mappingMap.put(pattern, mapping.getName());
            }
        }
    }

    // 通过URL的路径找到了对应的class
    public String getClz(String pattern) {
        String name = mappingMap.get(pattern);
        return entityMap.get(name);
    }
}
