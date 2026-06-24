package monster

import "testing"

func TestStore(t *testing.T) {
	monster := Monster{Name: "牛魔王", Age: 500, Skill: "吐火"}
	res := monster.Store()
	if !res {
		t.Fatalf("Store() failed")
	} else {
		t.Logf("Store() success")
	}
}

func TestReStore(t *testing.T) {
	var monster Monster
	res := monster.ReStore()
	if !res {
		t.Fatalf("ReStore() failed")
	} else {
		if monster.Name != "牛魔王" || monster.Age != 500 || monster.Skill != "吐火" {
			t.Fatalf("ReStore() failed")
		} else {
			t.Logf("ReStore() success")
		}
	}
}
